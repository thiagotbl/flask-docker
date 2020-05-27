from flask import Flask
from flask import request
from flask import jsonify

from candidates_repository import CandidatesRepository

app = Flask(__name__)

@app.route('/')
def similar_candidates():
    candidate_id = int(request.args.get('q'))

    similar_candidates = CandidatesRepository().get_similar(candidate_id)

    return jsonify(similar_candidates)

if __name__ == '__main__':
    CandidatesRepository().start()

    app.run(debug=True, host='0.0.0.0')
