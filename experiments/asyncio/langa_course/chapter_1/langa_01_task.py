
import asyncio
import time
import threading
import typing as t

asyncio.Future

## make the same with asyncio
# both coroutines get single instance of dict

async def mayhem(map: t.Mapping[str, int]) -> None:
    for _, value in map.items():
        print(f'sleeping for {value} seconds')
        await asyncio.sleep(value)

async def corrupted(map: t.Mapping[str, int]) -> None:
    map['bars'] = 12

async def main() -> None:
    # dict is shared between coroutines
    d = {'foo': 1, 'bar': 2, 'baz': 3}
    await asyncio.gather(
        mayhem(d),
        corrupted(d)
    )

if __name__ == '__main__':
    asyncio.run(main())