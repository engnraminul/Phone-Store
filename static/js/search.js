
const sendSearchData = (phone) => {
    $.ajax({
        type: 'POST',
        url:'phone/search/',
        data:{
            'csrfmiddlewaretoken': csrf,
            'phone':phone,
        },
        success: (res) => {
            console.log(res.data)
            const data = res.data
            result_box.innerHTML +=''

            if (Array.isArray(data)){
                result_box.innerHTML = "";
                data.forEach(phone=> {
                    result_box.innerHTML += `
                    <a href="${phone.slug}">
                    <div class="row m-0 p-0">
                        <div class="col-4">
                            <img src="${phone.thumbnail}" class="phone-img" alt="">  
                        </div>
                        <div class="col-8">
                            <p class="p-tag m-0" id="result_title">${phone.name}</p>
                        </div>

                    </div>
                    </a>
                    <hr>
                    
                    `
                })
                
            } else {
                if (search_input.value.lenght > 0) {
                    result_box.innerHTML = '<b>${data}</b>'
                } else {
                    result_box.classList.add('not-visible')
                }
            }
        },
        error: (err)=> {
            console.log(err)
        }
    })

}

const search_form = document.getElementById('search-form')
const search_input = document.getElementById('search-input')
const result_box = document.getElementById('results-box')
const csrf = document.getElementsByName('csrfmiddlewaretoken')[0].value




search_input.addEventListener('keyup', e=>{
    console.log(e.target.value)
    if (result_box.classList.contains('not-visible')){
        result_box.classList.remove('not-visible')
        
    }

    sendSearchData(e.target.value)
})

