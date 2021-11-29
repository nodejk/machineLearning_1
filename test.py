import csv
import argparse


print("here")
if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("--data", type=str)
    parser.add_argument("--eta")
    parser.add_argument("--threshold")

    args = parser.parse_args()

    path = args.data
    eta = float(args.eta)
    threshold = float(args.threshold)

    with open(path, 'r') as csvfile:
        my_reader = csv.reader(csvfile, delimiter=',')
        print("reading the file")
        xi = []
        for row in my_reader:
            xi.append(row)
        w0, w1, w2, x0 = 0, 0, 0, 1
        iteration = 0
        n = len(xi)
        sumofs2error_old = 0
        difference = 10000

        print('iteration_number' + ',' + 'weight0' + ',' + 'weight1' + ',' + 'weight2' + ',' + 'sum_of_squared_errors')
        while (difference > threshold):
            # sumofs2error_old = sumofs2error_new
            sumofs2error = 0
            gradientsum = [0, 0, 0]
            for i in range(0, n, 1):
                x1 = float(xi[i][0])
                x2 = float(xi[i][1])
                yi = float(xi[i][2])
                xibar = [x0, x1, x2]
                fofxibar = (w0 * x0) + (w1 * x1) + (w2 * x2)
                error = yi - fofxibar
                s2error = error * error
                sumofs2error = sumofs2error + s2error
                for j in range(3):
                    gradientsum[j] = gradientsum[j] + (xibar[j] * error)

            sumofs2error_new = sumofs2error
            result = str(iteration) + ',' + str(w0) + ',' + str(w1) + ',' + str(w2) + ',' + str(sumofs2error)
            w0 = w0 + gradientsum[0] * eta
            w1 = w1 + gradientsum[1] * eta
            w2 = w2 + gradientsum[2] * eta
            print(result)
            if iteration != 0:
                difference = abs(sumofs2error_new - sumofs2error_old)
                sumofs2error_old = sumofs2error_new

            iteration += 1


