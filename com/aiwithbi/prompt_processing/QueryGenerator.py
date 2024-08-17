from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
from com.aiwithbi.exceptions.ModelInferenceError import ModelInferenceError
import logging

class QueryGenerator:
    def __init__(self, model_name: str):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
        logging.info(f"Model {model_name} loaded successfully.")

    def process_prompt(self, prompt: str):
        try:
            inputs = self.tokenizer(prompt, return_tensors="pt", max_length=512, truncation=True)
            return inputs
        except Exception as e:
            logging.error(f"Error processing prompt: {str(e)}")
            raise ModelInferenceError(f"Error processing prompt: {str(e)}")

    def generate_sql_query(self, prompt: str):
        try:
            inputs = self.process_prompt(prompt)
            outputs = self.model.generate(inputs['input_ids'], max_length=512, num_beams=5, early_stopping=True)
            query = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
            logging.info(f"SQL query generated: {query}")
            return query
        except Exception as e:
            logging.error(f"Error generating SQL query: {str(e)}")
            raise ModelInferenceError(f"Error generating SQL query: {str(e)}")
