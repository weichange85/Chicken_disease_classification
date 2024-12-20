from cnnClassifier.constants import *
from cnnClassifier.utils.common import read_yaml_file, create_directories
from cnnClassifier.entity.config_entity import DataIngestionConfig, PrepareBaseModelConfig, PrepareCallbacksConfig, TrainingConfig, ModelEvaluationConfig
import os

class ConfigurationManager:
    def __init__(
            self,
            config_filepath = CONFIG_FILE_PATH,
            params_filepath = PARAMS_FILE_PATH
        ):
        self.config = read_yaml_file(config_filepath)
        self.params = read_yaml_file(params_filepath)

        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir = config.unzip_dir
        )

        return data_ingestion_config

    def get_prepare_base_model_config(self) -> PrepareBaseModelConfig:
        config = self.config.prepare_base_model
        params = self.params

        create_directories([config.root_dir])

        prepare_base_model_config = PrepareBaseModelConfig(
            root_dir=config.root_dir,
            base_model_path=config.base_model_path,
            updated_base_model_path=config.updated_base_model_path,
            params_image_size = params.IMAGE_SIZE,
            params_learning_rate = params.LEARNING_RATE,
            params_include_top = params.INCLUDE_TOP,
            params_weights = params.WEIGHTS,
            params_classes = params.CLASSES
        )

        return prepare_base_model_config

    def get_prepare_callback_config(self) -> PrepareCallbacksConfig:
        config = self.config.prepare_callbacks
        model_ckpt_dir = os.path.dirname(config.checkpoint_model_filepath)
        create_directories([
            Path(model_ckpt_dir),
            Path(config.tensorboard_root_log_dir)
        ])

        prepare_callback_config = PrepareCallbacksConfig(
            root_dir=Path(config.root_dir),
            tensorboard_root_log_dir=Path(config.tensorboard_root_log_dir),
            checkpoint_model_filepath=Path(config.checkpoint_model_filepath)
        )

        return prepare_callback_config
    
    def get_training_config(self) -> TrainingConfig:
        training_config = self.config.training
        prep_base_model_config = self.config.prepare_base_model
        training_data = os.path.join(self.config.data_ingestion.unzip_dir, "Chicken-fecal-images")
        create_directories([Path(training_config.root_dir)])
        params = self.params

        training_config = TrainingConfig(
            root_dir = Path(training_config.root_dir),
            trained_model_filepath = Path(training_config.trained_model_filepath),
            updated_base_model_path = Path(prep_base_model_config.updated_base_model_path),
            training_data = Path(training_data),
            params_epochs = params.EPOCHS,
            params_batch_size = params.BATCH_SIZE,
            params_augmentation = params.AUGMENTATION,
            params_image_size = params.IMAGE_SIZE
        )

        return training_config
        
    
    def get_model_evaluation_config(self) -> ModelEvaluationConfig:
        eval_config = ModelEvaluationConfig(
            model_path = self.config.training.trained_model_filepath,
            training_data = "artifacts\data_ingestion\Chicken-fecal-images",
            all_params = self.params,
            params_image_size = self.params.IMAGE_SIZE,
            params_batch_size = self.params.BATCH_SIZE,
        )
        
        return eval_config