import tensorflow as tf

from cnnClassifier.entity.config_entity import *
from cnnClassifier.utils.common import *
from cnnClassifier.config.configuration import *



class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config
    
    def valid_generator(self):

        datagenerator_kwargs = dict(
            rescale = 1./255,
            validation_split = 0.20
        )

        dataflow_kwargs = dict(
            target_size = self.config.params_image_size[:-1],
            batch_size = self.config.params_batch_size,
            interpolation = "bilinear"
        )

        valid_datagenerator = tf.keras.preprocessing.image.ImageDataGenerator(
            **datagenerator_kwargs
        )

        self.valid_generator = valid_datagenerator.flow_from_directory(
            directory = self.config.training_data,
            subset = "validation",
            shuffle= False,
            **dataflow_kwargs
        )


    @staticmethod
    def load_model(path: Path) -> tf.keras.models:
        return tf.keras.models.load_model(path)
    
    def evaluation(self):
        self.model = self.load_model(self.config.model_path)
        self.valid_generator()
        self.score = self.model.evaluate(self.valid_generator)
    
    def save_score(self):
        scores = {"loss": self.score[0], "accuracy": self.score[1]}
        save_json(out_filepath=Path("score.json"), data=scores)


if __name__=="__main__":
    config_manager = ConfigurationManager()
    eval_config = config_manager.get_model_evaluation_config()
    model_evaluation = ModelEvaluation(eval_config)
    model_evaluation.evaluation()
    model_evaluation.save_score()