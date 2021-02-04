from fastai.vision.all import load_learner
from webapp.HWES.utils.math_lib import Math
import base64

class Canvas():
    def __init__(self):
        self.model = load_learner('webapp/HWES/utils/export.pkl')
        self.math = Math()
        self.the_list = []

    def get_prediction(self, image_bytes, high_low):
        math = Math()
        data = str(image_bytes).split(',')[1]
        image = base64.b64decode(data)
        output = self.model.predict(image)
        high = max(high_low)
        low = min(high_low)
        if output[0] == 'times':
            output[0] = '*'
        self.the_list.append(str(output[0]))
        if '∫' in self.the_list:
            if len(self.the_list) > 1:
                return self.math.integration(self.the_list, high=high, low=low), output, self.the_list
            else:
                return '∫','∫',self.the_list
        elif 'sqrt' in self.the_list:
            if len(self.the_list) > 1:
                return self.math.sqrt(self.the_list), output, self.the_list
            else:
                return '√','√',self.the_list
        else:
            return self.math.just_maths(self.the_list), output, self.the_list

    def clear(self):
        self.the_list.clear()
