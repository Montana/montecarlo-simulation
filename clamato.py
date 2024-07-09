import random
import logging

class ClamatoCapitalMonteCarlo:
    def __init__(self, num_samples):
        self.num_samples = num_samples
        self.inside_circle = 0
        self.logger = self.setup_logger()

    def setup_logger(self):
        logger = logging.getLogger('ClamatoCapitalMonteCarlo')
        logger.setLevel(logging.DEBUG)
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        ch.setFormatter(formatter)
        logger.addHandler(ch)
        return logger

    def run_simulation(self):
        self.logger.info(f"Starting Monte Carlo simulation with {self.num_samples} samples.")
        
        for _ in range(self.num_samples):
            x, y = self.generate_random_point()
            if self.is_inside_circle(x, y):
                self.inside_circle += 1
        
        pi_estimate = self.calculate_pi()
        self.logger.info(f"Completed Monte Carlo simulation. Estimated value of π: {pi_estimate}")
        return pi_estimate

    def generate_random_point(self):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        self.logger.debug(f"Generated point ({x}, {y})")
        return x, y

    def is_inside_circle(self, x, y):
        inside = x**2 + y**2 <= 1
        self.logger.debug(f"Point ({x}, {y}) is {'inside' if inside else 'outside'} the circle")
        return inside

    def calculate_pi(self):
        pi_estimate = (self.inside_circle / self.num_samples) * 4
        self.logger.debug(f"Calculated π estimate: {pi_estimate}")
        return pi_estimate

if __name__ == "__main__":
    num_samples = 1000000
    clamato_capital = ClamatoCapitalMonteCarlo(num_samples)
    pi_estimate = clamato_capital.run_simulation()
    print(f"Clamato Capital's estimated value of π with {num_samples} samples: {pi_estimate}")
