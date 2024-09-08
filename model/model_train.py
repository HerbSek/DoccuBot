import pandas as pd
from simpletransformers.question_answering import QuestionAnsweringModel

def main():
    # Load the data
    data = pd.read_csv('qa3.csv')

    # Prepare the data for training
    train_data = [] 
    for index, row in data.iterrows():
        train_data.append({
            'context': row['context'],
            'qas': [{
                'question': row['question'],
                'id': str(index),
                'answers': [{
                    'text': row['answer'],
                    'answer_start': row['answer_start'],
                }]     
            }]
        })
    # print(train_data)



    model_args = {
        "n_best_size": 2,
        "max_seq_length": 384,
        "doc_stride": 128,
        "overwrite_output_dir": False,
        "learning_rate": 3e-3,
        "num_train_epochs": 5,
        "train_batch_size": 8
    }

    model = QuestionAnsweringModel('distilbert', 'distilbert-base-cased-distilled-squad', args=model_args,  use_cuda=False )

    try:
        model.train_model(train_data)
        model.save_model()

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__=='__main__':
    main()



