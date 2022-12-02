from tensorflow.keras.models import Model
from tensorflow.keras.layers import Dense, LSTM, Add, Dropout, Embedding, Reshape

class MergeDecoder(Model):

    def __init__(self, vocab_size, embbeding_dim, max_length) -> None:
        super(MergeDecoder, self).__init__(name='decoder')

        self.dropout1 = Dropout(0.5)
        self.dense1 =  Dense(256, activation='relu')

        self.Embedding = Embedding(vocab_size, embbeding_dim, mask_zero=True)
        self.dropout2 = Dropout(0.5)
        self.LSTM = LSTM(256)

        self.add = Add()
        self.dense2 = Dense(256, activation='relu')

        self.dense3 = Dense(vocab_size, activation='softmax')
    
    def call(self, inputs):
        
        InputA = inputs[0]
        InputB = inputs[1]

        A = self.dropout1(InputA)
        A = self.dense1(A)

        B = self.Embedding(InputB)
        B = self.dropout2(B)
        B = self.LSTM(B)

        decoder = self.add([A, B])
        decoder = self.dense2(decoder)

        outputs = self.dense3(decoder)

        return outputs


class InjectDecoder(Model):

    def __init__(self, vocab_size, embbeding_dim, max_length) -> None:
        super(InjectDecoder, self).__init__(name='decoder')
        
        self.dense1 =  Dense(4480, activation='relu')
        self.dropout1 = Dropout(0.5)
        self.reshape = Reshape(target_shape=(70, 64))

        self.Embedding = Embedding(vocab_size, embbeding_dim, mask_zero=True)
        self.dropout2 = Dropout(0.5)

        self.add = Add()        
        self.LSTM = LSTM(256)
        self.dense2 = Dense(256, activation='relu')
        self.dense3 = Dense(vocab_size, activation='softmax')
    
    def call(self, inputs):
        
        InputA = inputs[0]
        InputB = inputs[1]

        A = self.dense1(InputA)
        A = self.dropout1(A)
        A = self.reshape(A)
        
        B = self.Embedding(InputB)
        B = self.dropout2(B)
        
        inject = self.add([A, B])
        
        decoder = self.LSTM(inject)
        outputs = self.dense3(decoder)

        return outputs