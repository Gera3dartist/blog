
import asyncio
import time
import threading
import typing as t

class Mayhem(threading.Thread):
    def __init__(self, map: t.Mapping[str, int]) -> None:
        super().__init__()
        self.map = map
    
    def run(self) -> None:
        for _, value in self.map.items():
            print(f'sleeping for {value} seconds')
            time.sleep(value)

def main() -> None:
    d = {'foo': 1, 'bar': 2, 'baz': 3}
    m = Mayhem(d)
    m.start()
    # this will break the program because we are modifying the dictionary while the thread is running
    d['bars'] = 12

if __name__ == '__main__':
    main()