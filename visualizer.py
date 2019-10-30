import matplotlib.pyplot as plt
from matplotlib import animation
import random
import sys


class bar_det:
    def __init__(self, height, colors):
        self.height = height
        self.colors = colors


frames = []
arr = [random.randrange(1, 50, 1) for i in range(50)]
n = len(arr)


def partition(arr, low, high):
    i = (low-1)
    pivot = arr[high]

    for j in range(low, high):
        if arr[j] <= pivot:
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)


def quickSort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi-1)
        cols = ['black'] * n
        cols[low] = 'cyan'
        cols[high] = 'cyan'
        bars = bar_det([a for a in arr], cols)
        frames.append(bars)
        quickSort(arr, pi+1, high)
        cols = ['black'] * n
        cols[low] = 'cyan'
        cols[high] = 'cyan'
        bars = bar_det([a for a in arr], cols)
        frames.append(bars)


def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    L = [0] * (n1)
    R = [0] * (n2)
    for i in range(0, n1):
        L[i] = arr[l + i]

    for j in range(0, n2):
        R[j] = arr[m + 1 + j]

    i = 0
    j = 0
    k = l
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

    cols = ['black'] * n
    cols[l] = 'cyan'
    cols[r] = 'cyan'
    bars = bar_det([a for a in arr], cols)
    frames.append(bars)


def mergeSort(arr, l, r):
    if l < r:
        m = (l+(r-1))//2
        mergeSort(arr, l, m)
        mergeSort(arr, m+1, r)
        merge(arr, l, m, r)


def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            cols = ['black'] * n
            cols[j+1] = 'cyan'
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
            bars = bar_det([a for a in arr], cols)
            frames.append(bars)


def animate_graph():
    def barlist(j):
        return frames[j]

    fig = plt.figure()

    n = len(frames)  # Number of frames
    x = range(1, len(arr)+1)
    barcollection = plt.bar(x, barlist(0).height, color=barlist(0).colors)

    def animate(i):
        bars = barlist(i)
        hts = bars.height
        cols = bars.colors
        for i, b in enumerate(barcollection):
            b.set_height(hts[i])
            b.set_color(cols[i])

    anim = animation.FuncAnimation(fig, animate, repeat=False, blit=False, frames=n,
                                   interval=100)
    plt.show()


if sys.argv[1] == 'bubble-sort':
    bubbleSort(arr)
    animate_graph()
elif sys.argv[1] == 'merge-sort':
    mergeSort(arr, 0, n-1)
    animate_graph()
elif sys.argv[1] == 'quick-sort':
    quickSort(arr, 0, n-1)
    animate_graph()
