import numpy as np
def objective(x):
    return 2 * np.sin(x) + 3 * np.cos(2 * x) + 5 * np.sin(2 / 3 * x)

n = 10000
data_x = np.linspace(0, 4 * np.pi, n)
data_y = objective(data_x)

def simulated_anealing(objective, cooling_rate, n_iter):
    x_iter = np.zeros((n_iter, ))
    obj_iter = np.zeros((n_iter, ))
    
    T = 1.0
    def cool(T):
        return cooling_rate * T
    
    index = 7000
    curr_x = data_x[index]
    curr_obj = objective(curr_x)

    best_x = curr_x
    best_obj = curr_obj

    for i in range(n_iter):
        T = cool(T)

        index = np.random.choice(n)
        new_x = data_x[index]
        new_obj = objective(new_x)

        if (new_obj >  curr_obj) or (np.random.rand() < np.exp((new_obj - curr_obj) / T)):
            curr_x = new_x
            curr_obj = new_obj

        if curr_obj > best_obj:
            best_x = curr_x
            best_obj = curr_obj

        x_iter[i] = best_x
        obj_iter[i] = best_obj

    return x_iter, obj_iter

x_iter, obj_iter = simulated_anealing(objective, cooling_rate=0.9, n_iter=100)
best_index = np.argmax(obj_iter)
print("best x: {}, best objective: {}".format(x_iter[best_index], obj_iter[best_index]))