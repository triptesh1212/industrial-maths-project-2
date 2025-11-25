import matplotlib.pyplot as plt
import numpy as np

def plot_opinions(agents_history, agents_initial, advertisers_history=None, advertisers_initial=None, rounds=10, alpha=0.6):

    fig, ax = plt.subplots(figsize=(8,4))  # create figure & axes

    colors = plt.cm.rainbow(agents_initial)

    for i in range(len(agents_initial)):
        ax.plot(range(rounds+1), agents_history[:, i], color=colors[i], alpha=alpha, linewidth=0.6)

    if advertisers_history is not None:
        for i in range(len(advertisers_initial)):
            ax.plot(range(rounds+1), advertisers_history[:, i], color="black", alpha=0.05, linewidth=0.6)
    else:
        print('No advertisers')

   
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

def plot_opinions_grid(
    agents_history, agents_initial,
    advertisers_history=None, advertisers_initial=None,
    rounds=10, alpha=0.6, ax=None
):

    # If no axis is passed, create one
    if ax is None:
        fig, ax = plt.subplots(figsize=(8,4))

    colors = plt.cm.rainbow(agents_initial)

    for i in range(len(agents_initial)):
        ax.plot(range(rounds+1), agents_history[:, i], color=colors[i], alpha=alpha, linewidth=0.6)

    if advertisers_history is not None:
        for i in range(len(advertisers_initial)):
            ax.plot(range(rounds+1), advertisers_history[:, i], color="black", alpha=0.05, linewidth=0.6)
    else:
        print('No advertisers')


    # sm = plt.cm.ScalarMappable(cmap=plt.cm.rainbow)
    # sm.set_array(agents_initial)
    # cbar = plt.colorbar(sm, ax=ax)
    # cbar.set_label("Initial opinion value")

def plot_methods(agents_history, alpha=1, tolerance=0.05, target=1, ax=None, colour=None, method=None, linewidth=1.5):
    
    time = agents_history.shape[0]
    mask = np.abs(agents_history - target) < tolerance #checks for opinions near 1, 1 for true, 0 false
    counts = np.sum(mask, axis=1) #counts number of opinions near 1 at certain time step

    # If no axis is passed, create one
    if ax is None:
        fig, ax = plt.subplots(figsize=(8,4))

    ax.plot(range(time), counts, alpha=alpha, color = colour, label=method, linewidth=linewidth)
    print(f'colour {colour} was used')

    ax.set_xlabel("Time")
    ax.set_ylabel(rf"Number of opinions within tolerance $\varepsilon$ {target}")

