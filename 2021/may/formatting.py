# the f formatting

class Comedian:
    def __init__(self, first_name, last_name, age) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.age}"

    def __repr__(self) -> str:
        return f'{self.first_name} {self.last_name} {self.age} Surprise!!!!'


new_comedian = Comedian("Ujjwal", "Singh", 35)
print (f"{new_comedian}")
print (f"{new_comedian!r}")

## Multiline
name = "Eric"
profession = "Comedian"
message = (
    f"Hi {name} ."
    f"You are in profession {profession}n"
)

print (message)