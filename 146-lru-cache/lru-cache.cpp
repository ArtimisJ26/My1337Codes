struct Node {
    int key, value;
    Node* prev;
    Node* next;

    Node(int k, int v) {
        key = k;
        value = v;
        prev = nullptr;
        next = nullptr;
    }
};

class LRUCache {
    int capacity;
    unordered_map<int, Node*> cache;
    Node* head;
    Node* tail;
public:
    LRUCache(int capacity) {
        this->capacity = capacity;
        head = new Node(-1, -1);
        tail = new Node(-1, -1);
        head->next = tail;
        tail->prev = head;
    }
    
    int get(int key) {
        if (cache.find(key) == cache.end()) return -1;

        Node* node = cache[key];
        removeNode(node);
        addNode(node);
        return node->value;
    }
    
    void put(int key, int value) {
        if (cache.find(key) != cache.end()) {
            Node* oldNode = cache[key];
            removeNode(oldNode);
            delete(oldNode);
        }

        // create a node
        Node* newNode = new Node(key, value);
        
        // add the node to DLL
        addNode(newNode);

        // Add the key and node address to the cacheMap
        cache[key] = newNode;

        if (cache.size() > capacity) {
            // Find node at tail
            Node* lastNode = tail->prev;
            // Delete key from cache
            cache.erase(lastNode->key);
            // remove node from tail
            removeNode(lastNode);
            delete(lastNode);
        }
    }

    void addNode(Node* node) {
        Node* nextNode = head->next;
        head->next = node;
        node->prev = head;
        node->next = nextNode;
        nextNode->prev = node;
    }

    void removeNode(Node* node) {
        Node* nextNode = node->next;
        if (node->prev) {
            Node* prevNode = node->prev;
            prevNode->next = nextNode;
            nextNode->prev = prevNode;
        }
    }
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */