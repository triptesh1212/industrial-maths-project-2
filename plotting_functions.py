import matplotlib.pyplot as plt
import numpy as np

def plot_opinions(agents_history, agents_initial, rounds, alpha=0.6):

    plt.figure(figsize=(8, 4))
    colors = plt.cm.rainbow(agents_initial)

    for i in range(len(agents_initial)):
        plt.plot(range(rounds), agents_history[:, i], color=colors[i], alpha=alpha)

    plt.xlabel("Time step")
    plt.ylabel("Opinion")
    plt.title("Opinion of all agents over time")
    plt.show()

