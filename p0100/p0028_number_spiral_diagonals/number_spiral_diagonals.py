import numpy as np

def spiralRecusive(N):

    if N % 2 == 0 or N < 0:
        raise ValueError()

    if N == 1:
        return np.array([[1]], dtype=np.uint32)

    minispiral = spiralRecusive(N - 2)
    spiralMatrix = np.empty((N,N), dtype=np.uint32)
    spiralMatrix[1:N - 1, 1:N - 1] = minispiral

    initSpiral = (N - 2) * (N - 2) + 1
    spiralMatrix[1:N, N - 1] = np.arange(initSpiral, initSpiral + N - 1)
    
    initSpiral += (N - 1)
    spiralMatrix[N - 1, 0:N - 1] = np.arange(initSpiral, initSpiral + N - 1)[::-1]

    initSpiral += (N - 1)
    spiralMatrix[0:N - 1, 0] = np.arange(initSpiral, initSpiral + N - 1)[::-1]

    initSpiral += (N - 1)
    spiralMatrix[0, 1: N] = np.arange(initSpiral, initSpiral + N - 1)

    return spiralMatrix



def spiralIterative(M):

    if M % 2 == 0 or M < 0:
        raise ValueError()

    spiralMatrix = None
    minispiral = np.array([[1]], dtype=np.uint32)

    if M == 1:
        return minispiral
    
    for N in range(3, M + 1, 2):

        spiralMatrix = np.empty((N,N), dtype=np.uint32)
        spiralMatrix[1:N - 1, 1:N - 1] = minispiral

        initSpiral = (N - 2) * (N - 2) + 1
        spiralMatrix[1:N, N - 1] = np.arange(initSpiral, initSpiral + N - 1)
        
        initSpiral += (N - 1)
        spiralMatrix[N - 1, 0:N - 1] = np.arange(initSpiral, initSpiral + N - 1)[::-1]

        initSpiral += (N - 1)
        spiralMatrix[0:N - 1, 0] = np.arange(initSpiral, initSpiral + N - 1)[::-1]

        initSpiral += (N - 1)
        spiralMatrix[0, 1: N] = np.arange(initSpiral, initSpiral + N - 1)

        minispiral = spiralMatrix

    return spiralMatrix





if __name__ == '__main__':
    N = 1001
    spiralMatrix = spiralIterative(N)
    result = np.sum(spiralMatrix.diagonal() + np.flipud(spiralMatrix).diagonal()) - 1
    print(result) 