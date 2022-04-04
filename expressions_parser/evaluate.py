
class Evaluate:
    infix = '0'
    posfix = '0'
    result = 0
    convert = False
    
    def __init__(self,logger=None,expression='0'):
        if logger:
            self.logger = logger
        else:
            import logging
            logging.basicConfig(level=logging.DEBUG)
            self.logger = logging.getLogger(__name__)
        self.infix = expression
        self.add_stack()
        
    def add_stack(self):
        self.__stack = Stack()
        
    def __is_float(self, decimal):
        try:
            float(decimal)
            return True
        except ValueError:
            return False
     
    def __convert(self, tokens):
        previous = {}
        previous['*'] = 3
        previous['/'] = 3
        previous['+'] = 2
        previous['-'] = 2
        previous['('] = 1
        
        posfix = []
        
        for token in tokens:
            if token.isnumeric():
                posfix.append(token)
            elif self.__is_float(token) == True:
                posfix.append(token)
            elif token.isidentifier():
                posfix.append(token)
            elif token == '(':
                self.__stack.push(token)
            elif token == ')':
                while True:
                    temp = self.__stack.pop()
                    if temp is None or temp == '(':
                        break
                    elif not temp.isidentifier():
                        posfix.append(temp)
                
            else:
                if not self.__stack.empty():
                    temp = self.__stack.peek()
                
                    while not self.__stack.empty() and previous[temp] >= previous[token] and token.isidentifier():
                        posfix.append(self.__stack.pop())
                        temp = self.__stack.peek()
                    
                self.__stack.push(token)
                    
        while not self.__stack.empty():
            posfix.append(self.__stack.pop())
        
        ans = ''
        for x in ans:
            ans += x + ' '
        
        return ans[:-1]
                
    def __calc_reversed_polish(self, expression):
     
        pila = []
     
        for valor in expression.split(' '):
            if valor in ['-', '+', '*', '/']:
                op1 = pila.pop()
                op2 = pila.pop()
                if valor=='-': resultado = op2 - op1
                if valor=='+': resultado = op2 + op1
                if valor=='*': resultado = op2 * op1
                if valor=='/': resultado = op2 / op1
                pila.append(resultado)
            else:
                pila.append(float(valor))

        return pila.pop()
    
    def infix_to_posfix(self):
        try:
            self.postfix = self.__convert([chr for chr in self.infix.replace(' ','')])
            self.convert= True
        except ValueError:
            self.postfix = '0'
    
    def calc_reversed_polish(self,from_sup=None):
        try:
            self.result = self.__calc_reversed_polish(self.postfix)
            if not from_sup:
                self.logger.debug('Expresion evaluada {}'.format(self.result))
        except ValueError:
            self.result = None
            self.logger.error("No se ha podido evaluar la expression")
        return self.result
    
    def evaluate(self):
        try:
            if not self.convert:
                self.infix_to_posfix()
            self.calc_reversed_polish(True)
            msg = 'Result:\t{}'.format(self.result)
            self.logger.info(msg)
        except:
            self.result = None
            msg = 'Can't evaluate'
            self.logger.error(msg)
        return self.result
    
    def replace_expression(self, new):
        self.infix = new
        self.postfix = '0'
        self.result = 0
        self.convert = False
    
    def evaluate_new(self, new):
        self.infix = new
        self.postfix = '0'
        self.result = 0
        self.convert = False
        self.evaluate()