from pyscript import document, when

grade7 = {"Raymond Manalansan", "Maya Angeles"}
grade8 = {"Bernadine Santos", "Jiwon Son"}
grade9 = {"Tua Mandap", "Aubrey Cabrera"}
grade10 = {"Isabelle Rivera", "Riona Narciso"}

new_students = set()

def render_roster():
    master_set = grade7 | grade8 | grade9 | grade10 | new_students
    
    total_count = len(master_set)
    
    formatted_students = ", ".join(sorted(master_set))
    
    output_div = document.querySelector("#OUTPUT")
    output_div.innerHTML = f"""
        <div class="alert alert-danger">
            <h5 class="alert-heading">Total Students: <span class="badge bg-danger">{total_count}</span></h5>
            <hr>
            <p class="mb-0"><strong>Full Student List:</strong><br>{formatted_students}</p>
        </div>
    """

@when("click", "#add-btn")
def add_student(event):
    first = document.querySelector("#firstname").value.strip()
    last = document.querySelector("#lastname").value.strip()
    
    if first or last:
        new_entry = f"{first} {last}".strip()
        new_students.add(new_entry)
    
    document.querySelector("#firstname").value = ""
    document.querySelector("#lastname").value = ""
    
    render_roster()

render_roster()