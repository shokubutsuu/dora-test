from dora import Node


def main():
    node = Node()

    for event in node:
        if event["type"] == "STOP":
            break

        if event["type"] == "INPUT" and event["id"] == "tick":
            count = event["value"][0].as_py()
            print(f"received tick: {count}", flush=True)


if __name__ == "__main__":
    main()
