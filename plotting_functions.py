import matplotlib.pyplot as plt
import numpy as np

def plot_opinions(agents_history, agents_initial, rounds, alpha=0.6):

    fig, ax = plt.subplots(figsize=(8,4))  # create figure & axes

    colors = plt.cm.rainbow(agents_initial)

    for i in range(len(agents_initial)):
        plt.plot(range(rounds+1), agents_history[:, i], color=colors[i], alpha=alpha)

    for i in range(len(agents_initial)):
        ax.plot(range(rounds+1), agents_history[:, i], color=colors[i], alpha=alpha)
   
    plt.xlabel("Time step")
    plt.ylabel("Opinion")
    plt.title("Opinion of all agents over time")

    #colour bar
    sm = plt.cm.ScalarMappable(cmap=plt.cm.rainbow)
    sm.set_array(agents_initial)
    cbar = plt.colorbar(sm, ax=ax)  
    cbar.set_label("Initial opinion value")

    plt.tight_layout()
    plt.show()


def plot_opinion_change(agents_history, agents_initial, rounds, alpha=0.6):

    fig, ax = plt.subplots(figsize=(8,4))  # create figure & axes

    colors = plt.cm.rainbow(agents_initial)

    agents_change = agents_history[1:, :] - agents_history[:-1, :] # 0-1, 1-2. 2-3, ..., 9-10

    for i in range(len(agents_initial)):
        ax.plot(range(0, rounds), agents_change[:, i], color=colors[i], alpha=alpha, linewidth=0.7)

    ax.set_xlabel("Time (t)")
    ax.set_ylabel("Opinion change from t to t+1")
    ax.set_title("Opinion change of all agents over time")

    #colour bar
    sm = plt.cm.ScalarMappable(cmap=plt.cm.rainbow)
    sm.set_array(agents_initial)
    cbar = plt.colorbar(sm, ax=ax)  
    cbar.set_label("Initial opinion value")

    plt.tight_layout()
    plt.show()

