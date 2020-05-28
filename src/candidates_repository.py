from threading import Lock
from typing import Optional
from os import path
import turicreate

class SingletonMeta(type):
    _instance = None
    _lock: Lock = Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if not cls._instance:
                cls._instance = super().__call__(*args, **kwargs)

        return cls._instance

class CandidatesRepository(metaclass=SingletonMeta):
    _model = None

    # TODO read weights from env vars or something else
    _weights = {
        'career': 0.5,
        'main_skills': 0.7,
        'secondary_skills': 0.3,
        'companies': 0.7,
        'jobs': 0.7,
        'education': 0.7,
        'contract_type': 0.3,
        'wage_claim': 0.3
    }

    # TODO new thread, train, and sync?
    def update(self) -> None:
        self.start()

    def start(self) -> None:
        if path.exists('jarvis.model'):
            self._model = turicreate.load_model('jarvis.model')
        else:
            self._model = self._train_model_and_persist()

    def get_similar(self, id: int) -> dict:
        candidates = self._model.recommend_from_interactions([id], 10)
        result = []

        for candidate in candidates[0:10]:
            result.append({
                'id': candidate['candidate_id'],
                'score': candidate['score']
            })

        return result

    def _train_model_and_persist(self):
        # TODO read data from S3
        data = turicreate.SFrame(self._data_path())

        model = turicreate.recommender.item_content_recommender.create(
            data, 'candidate_id', weights=self._weights
        )
        model.save('jarvis.model')
        return model

    def _data_path(self):
        basepath = path.dirname(__file__)
        filepath = path.abspath(
            path.join(basepath, 'data', 'marketplace-candidates.csv')
        )

        return filepath
