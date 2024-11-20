from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.prepare_callbacks import PrepareCallback
from cnnClassifier import logger


STAGE_NAME = "Prepare Callbacks Stage"

class PrepareCallbacksTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
            
        config = ConfigurationManager()
        prepare_callbacks_config = config.get_prepare_callback_config()
        prepare_callbacks = PrepareCallback(config=prepare_callbacks_config)
        callback_list = prepare_callbacks.get_tb_ckpt_callbacks()



if __name__ == "__main__":
    try:
        obj = PrepareCallbacksTrainingPipeline()
        obj.main()
    except Exception as e:
        raise e