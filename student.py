import argparse
import csv

def output_function(w0, w1, w2, x1, x2):

    return w0 * 1 + w1 * x1 + w2 * x2

print("oisdjflk")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", type = str)
    parser.add_argument("--eta")
    parser.add_argument("--threshold")

    args = parser.parse_args()

    path = args.data
    eta = float(args.eta)
    threshold = float(args.threshold)


    w0 = 0
    w1 = 0
    w2 = 0
    iteration = 0


    training_data = []
    with open(path) as f:
        cf = csv.reader(f)

        for row in cf:
            training_data.append([float(row[0]), float(row[1]), float(row[2])])


    # print(training_data)

    difference = float("inf")
    error0 = 0

    while(difference > threshold):

        error = 0
        gradient0 = 0
        gradient1 = 0
        gradient2 = 0

        for data in training_data:
            output = output_function(w0, w1, w2, data[0], data[1])
            # print(output)

            error += (data[2] - output) * (data[2] - output)

            gradient0 += data[2] - output
            gradient1 += (data[2] - output) * data[0]
            gradient2 += (data[2] - output) * data[1]

            # print(gradient0, gradient1, gradient2)


        print(str(iteration) + "," + str(w0) + "," + str(w1) + "," + str(w2) + "," + str(error))

        w0 = w0 + eta * gradient0
        w1 = w1 + eta * gradient1
        w2 = w2 + eta * gradient2
        iteration += 1

        difference = abs(error - error0)

        error0 = error
















