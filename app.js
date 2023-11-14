const propertylist= document.querySelector('.row');
const resource_path = './js/data/properties.json';

async function getProperties() {
    try {
        const res = await fetch(resource_path);
        return await res.json();
    } catch (error) {
        console.log(error);
    }
}

async function renderProperties() {
    let props = await getProperties();
    let html = '';
    props.forEach(p => {
       let htmlSegment = `<div class="col-md-4">
        <div class="card mb-4 box-shadow">
          <img class="card-img-top" src="${p.primaryURL}" alt="Thumbnail [100%x225]" >
          <div class="list-card-info">  
                <a href="detail.html" class="list-card-link list-card-link-top-margin" tabindex="0">
               <address class="list-card-addr">${p.Address}</address></a> 
              <div class="list-card-footer">
               <p class="list-card-extra-info">${p.agent}</p>
              </div>
              <div class="list-card-heading">
                  <div class="list-card-price">$${p.price}</div>
                  <ul class="list-card-details">
                    <li class="">${p.bds}<abbr class="list-card-label"> bds</abbr></li>
                    <li class="">${p.ba}<abbr class="list-card-label"> ba</abbr></li>
                    <li class="">${p.sqft}<abbr class="list-card-label"> sqft</abbr></li>
                    <li class="list-card-statusText">- ${p.type} for rent</li>
                   </ul>
               </div>
             </div>
           </div>
          </div>
        `;

        html += htmlSegment;
    });

    propertylist.innerHTML = html;
}

renderProperties()
