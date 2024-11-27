from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.prepare_callbacks import PrepareCallback
from cnnClassifier.components.training import Training
from cnnClassifier import logger


STAGE_NAME = "Training Stage"

class TrainingPipeline:
    def __init__(self):
        pass

    def main(self):
            
        config = ConfigurationManager()
        training_config = config.get_training_config()
        prep_callbacks_congfig = config.get_prepare_callback_config()
        
        prep_callbacks_obj = PrepareCallback(prep_callbacks_congfig)
        training_obj = Training(training_config)

        callbacks_list = prep_callbacks_obj.get_tb_ckpt_callbacks()
        training_obj.get_base_model()
        training_obj.train_valid_generator()
        training_obj.train(callbacks_list)

if __name__ == "__main__":
    try:
        obj = TrainingPipeline()
        obj.main()
    except Exception as e:
        raise e