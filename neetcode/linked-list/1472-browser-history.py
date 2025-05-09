class ListNode:
    def __init__(self, url=None, prev=None, next=None):
        self.url = url
        self.prev = prev
        self.next = next


class BrowserHistory:
    def __init__(self, homepage: str):
        self.home = ListNode(homepage, None, None)
        self.current = self.home
        self.size = 1

    def visit(self, url: str) -> None:
        new_page = ListNode(url=url, prev=self.current, next=None)
        self.current.next = new_page
        self.current = new_page
        

    def back(self, steps: int) -> str:
        counter = 0
        while self.current.prev and counter < steps:
            self.current = self.current.prev
            counter += 1
        return self.current.url
        

    def forward(self, steps: int) -> str:
        counter = 0
        while self.current.next and counter < steps:
            self.current = self.current.next
            counter += 1
        return self.current.url