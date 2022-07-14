//Set variables
const affection_level = document.querySelector('#affection_level')

const form = document.querySelector('#form_cat')
const select = document.querySelector('#breed')

// To display the breed in the select option box after a user have selected the breed
select.addEventListener('change', (e) => {form.submit()})
select.value = breed
select.text = breed

// To display number of paws
for(i=0; i< affection_level_paws; i++){
  affection_level.innerHTML += '<span class="fa-lg fa fa-paw mx-auto"></span><span> </span>'
}