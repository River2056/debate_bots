from config import bots


def main():
    topic = input("topic to debate: ")
    input_rounds = int(input("rounds to debate: "))
    # each bot said a thing, counts as a round
    total_rounds = input_rounds * len(bots)

    for bot in bots:
        bot.topic = topic
        bot.total_rounds = total_rounds

    all_msgs = []
    rounds = 0
    while True:
        all_msgs.append(bots[rounds % len(bots)].debate(rounds, all_msgs))
        rounds += 1

        if rounds == total_rounds:
            break

    filename = f"./{topic[0:30].replace(" ", "_")}.txt"
    with open(filename, "wt", encoding="utf8") as output:
        for msg in all_msgs:
            print(msg)
            output.write(f"id: {msg.id}")
            output.write("\n")
            output.write(msg.msg)
            output.write("\n")


if __name__ == "__main__":
    main()
