import pyarrow as pa
from dora import Node


def main():
    node = Node()
    count = 1

    for event in node:
        if event["type"] == "STOP":
            break

        if event["type"] == "INPUT" and event["id"] == "interval":
            node.send_output(
                "tick",
                pa.array([count], type=pa.int64()),
                event["metadata"],
            )
            count += 1


if __name__ == "__main__":
    main()
