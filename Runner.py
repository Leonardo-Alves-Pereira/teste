import sys
import concurrent.futures
from unittest import TestLoader, TextTestResult, TextTestRunner, TestCase
from Src.Scripts.test_Google_Search import Google_Search
from selenium import webdriver

class CustomTextTestResult(TextTestResult):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.errors_captured = []

    def addError(self, test, err):
        test_name = self.getDescription(test)
        err_class, err_instance, _ = err
        error_message = f"Erro no teste {test_name}: {err_class.__name__} - {err_instance}"
        self.errors_captured.append(error_message)
        super().addError(test, err)

class CustomTextTestRunner(TextTestRunner):
    def run(self, test):
        result = self._makeResult()
        result.failfast = self.failfast
        result.buffer = self.buffer
        result.tb_locals = self.tb_locals

        test(result)

        return result

    def _makeResult(self):
        return CustomTextTestResult(self.stream, self.descriptions, self.verbosity)

def run_test(test_class):
    loader = TestLoader()
    suite = loader.loadTestsFromTestCase(test_class)

    custom_runner = CustomTextTestRunner(verbosity=2)
    custom_result = custom_runner.run(suite)

    # A variável errors_captured agora contém as mensagens detalhadas de erro
    for error_message in custom_result.errors_captured:
        print(error_message.split('\n', 1)[0])  # Imprime apenas a primeira linha da mensagem

if __name__ == "__main__":
    # Lista de classes de teste a serem executadas simultaneamente
    test_classes = [Google_Search] * 8

    # Crie um pool de threads para executar os testes simultaneamente
    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:
        executor.map(run_test, test_classes)
