init python:
    def check_filter(filter, data): #проверяет сходится-ли объект с фильтром filter (словарь)
        for var1 in filter:
            if data.has_key(var1) != True or data[var1] != filter[var1]:
                return False
        return True
