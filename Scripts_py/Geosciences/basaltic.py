# ejemplo de nested function
def main_function():
    rock = "basaltic"

    def nested_function():
        print("Some vulcanoes produce", rock, "rocks")
    
    nested_function()

main_function()
