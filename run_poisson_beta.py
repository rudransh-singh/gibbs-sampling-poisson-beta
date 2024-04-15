from poisson_beta.poisson_beta import PoissonBeta

if __name__ == "__main__":
    input_file = "data/test.txt"
    output_file = "result.txt"
    num_iterations = 30

    pb = PoissonBeta(input_file, output_file, num_iterations)
    pb.run()