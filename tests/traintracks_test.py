import unittest
import numpy as np

from pathlib import Path

import commons.utils as utils
from commons.traintracks import TrainTracker

HOME = str(Path.home())
FS_HOME = f'{HOME}/Work/devdata'


class TestTrainTracker(unittest.TestCase):

    def test_basic(self):
        tracker = TrainTracker(root=f'{FS_HOME}/traintracks-test/experiment', mem_threshold=200)
        tracker.log_conf({
            'property 1': 1,
            'hello': 'x'
        })
        tracker.save_module(utils)
        tracker.add_plot('loss', 1000, 'iteration', last_n=100)
        tracker.add_plot('loss2', 2000, 'iteration', movingavg=100, last_n=500)

        tracker.add_plot('many_vals', 2000, 'iteration', movingavg=100, last_n=500)

        tracker.add_callback(lambda: print(tracker.counters['iteration']), 2000, 'iteration')

        for epoch in range(5):

            tracker.start('epoch')

            for i in range(5000):
                tracker.start('iteration')

                loss = 100 + np.random.randn(1)[0] * 10
                tracker.log_metric('loss', loss)
                tracker.log_metric('loss2', loss)

                tracker.log_metric('many_vals', list(np.random.randn(33)))

                if i % 500 == 0:
                    print(f'Epoch {epoch}, iter {i} --> loss={tracker.get_metric("loss", movingavg=200):.2f}')
