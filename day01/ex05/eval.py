class Evaluator:
    @staticmethod
    def zip_evaluate(coefs, words):
        if not isinstance(coefs, list) or not isinstance(words, list):
            return -1
        if not all(isinstance(c, (int, float)) for c in coefs) or not all(isinstance(w, str) for w in words):
            return -1
        if len(coefs) != len(words):
            return -1
        return sum(len(word) * c for c, word in zip(coefs, words))

    @staticmethod
    def enumerate_evaluate(coefs, words):
        if not isinstance(coefs, list) or not isinstance(words, list):
            return -1
        if not all(isinstance(c, (int, float)) for c in coefs) or not all(isinstance(w, str) for w in words):
            return -1
        if len(coefs) != len(words):
            return -1
        return sum(len(word) * c for i, (c, word) in enumerate(zip(coefs, words)))

words = ["Le", "Lorem", "Ipsum", "est", "simple"]
coefs = [1.0, 2.0, 1.0, 4.0, 0.5]

print(Evaluator.zip_evaluate(coefs, words))
print(Evaluator.enumerate_evaluate(coefs, words))


words = ["Le", "Lorem", "Ipsum", "n’", "est", "pas", "simple"]
coefs = [0.0, -1.0, 1.0, -12.0, 0.0, 42.42]
print(Evaluator.zip_evaluate(coefs, words))
print(Evaluator.enumerate_evaluate(coefs, words))

print(Evaluator.zip_evaluate(None, None))
print(Evaluator.enumerate_evaluate(None, None))

print(Evaluator.zip_evaluate([1, 2, 3], []))
print(Evaluator.enumerate_evaluate([1, 2, 3], []))

print(Evaluator.zip_evaluate([1, 2, 3], ["word", 2, "wordo"]))
print(Evaluator.enumerate_evaluate([1, 2, 3], ["word", 2, "wordo"]))

print(Evaluator.zip_evaluate([1, 2, 3], ["word", "word", "word"]))
print(Evaluator.enumerate_evaluate([1, 2, 3], ["word", "word", "word"]))

print(Evaluator.zip_evaluate([1, 2], ["word", "word"]))
print(Evaluator.enumerate_evaluate([1, 2], ["word", "word"]))

print(Evaluator.zip_evaluate([1], ["word"]))
print(Evaluator.enumerate_evaluate([1], ["word"]))