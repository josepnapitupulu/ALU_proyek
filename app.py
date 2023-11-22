from flask import Flask, render_template, request, jsonify
import numpy as np

app = Flask(__name__)

def calculate_distance(point1, point2):
    return np.linalg.norm(point1 - point2)

def calculate_total_distance(path, points):
    total_distance = 0
    for i in range(len(path) - 1):
        total_distance += calculate_distance(points[path[i]], points[path[i + 1]])
    return total_distance

def run_pso_algorithm(points, swarm_size, iterations):
    num_points = len(points)
    particles = np.random.permutation(num_points).tolist()

    global_best = particles.copy()
    global_best_distance = calculate_total_distance(global_best, points)

    for _ in range(iterations):
        for i in range(swarm_size):
            new_particle = np.random.permutation(num_points).tolist()

            new_particle_distance = calculate_total_distance(new_particle, points)

            if new_particle_distance < calculate_total_distance(particles[i], points):
                particles[i] = new_particle.copy()

                if new_particle_distance < global_best_distance:
                    global_best = new_particle.copy()
                    global_best_distance = new_particle_distance

    return global_best

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run_pso', methods=['POST'])
def run_pso():
    data = request.get_json()
    points = np.array(data['points'])
    swarm_size = data['swarm_size']
    iterations = data['iterations']

    best_path = run_pso_algorithm(points, swarm_size, iterations)

    return jsonify({'best_path': best_path.tolist()})

if __name__ == '__main__':
    app.run(debug=True)
