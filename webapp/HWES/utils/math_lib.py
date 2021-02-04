from scipy.integrate import quad
from Equation import Expression

class Math():
    def integration(self,this_list, low = 0, high = 1):
        class_list = this_list.copy()
        class_list.remove('∫')
        function_list = ['*x' if ele == 'X' and class_list[idx-1].isnumeric() else  '1*x' if ele == 'X' else ele for idx,ele in enumerate(class_list)]
        try:
            for idx,element in enumerate(function_list):
                if 'x' in element and function_list[idx+1].isnumeric():
                    function_list[idx+1] = '**' + function_list[idx+1]
        except:
            pass
        function = ''.join(i for i in function_list)
        fn = Expression(function,'x')
        itg  = quad(fn,low,high)
        return itg[0]

    def just_maths(self,this_list):
        expression = ''.join(i for i in this_list)
        try:
            return eval(expression)
        except:
            if '+' in this_list:
                return this_list[-2]
            elif '-' in this_list:
                return this_list[-2]

    def sqrt(self, this_list):
        list_copy = this_list.copy()
        list_copy.remove('sqrt')
        sqrot = ''.join(i for i in list_copy)
        return int(sqrot) ** (1/2)
