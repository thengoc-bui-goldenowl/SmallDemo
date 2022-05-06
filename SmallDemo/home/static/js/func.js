// const data = {

//     "project": [{ "id": "1", "link": "#1", "name": "Doe", "des": "d1", "start": "12/12/2019", "end": "1/3/2020", "Dev": "Doe" },
//         { "id": "2", "link": "#2", "name": "Kai", "des": "d1", "start": "12/1/2019", "end": "1/3/2020", "Dev": "Da Ve" },
//         { "id": "3", "link": "#3", "name": "Kid", "des": "d1", "start": "12/4/2019", "end": "1/1/2020", "Dev": "Jack" },
//         { "id": "4", "link": "#4", "name": "Gin", "des": "d1", "start": "12/2/2019", "end": "1/3/2020", "Dev": "Maya" },
//         { "id": "5", "link": "#5", "name": "Lao", "des": "d1", "start": "12/5/2019", "end": "1/3/2020", "Dev": "Kin" },
//         { "id": "6", "link": "#6", "name": "Mana", "des": "d1", "start": "12/12/2019", "end": "1/3/2020", "Dev": "Jack" },
//         { "id": "7", "link": "#7", "name": "Near", "des": "d1", "start": "12/12/2019", "end": "1/3/2020", "Dev": "Kin" },
//         { "id": "8", "link": "#8", "name": "Zoro", "des": "d1", "start": "12/12/2019", "end": "1/3/2020", "Dev": "Kay" },
//         { "id": "9", "link": "#9", "name": "Sasuke", "des": "d1", "start": "12/12/2019", "end": "1/3/2020", "Dev": "Kin" }
//     ],
//     "dev": [
//         { "id": "1", "name": "Doe", "link": "#a", "Status": "0" },
//         { "id": "1", "name": "Jack", "link": "#a", "Status": "1" },
//         { "id": "1", "name": "Maya", "link": "#a", "Status": "0" },
//         { "id": "1", "name": "Kin", "link": "#a", "Status": "1" },
//         { "id": "1", "name": "Jack", "link": "#a", "Status": "0" },
//         { "id": "1", "name": "Kay", "link": "#a", "Status": "0" }
//     ]
// };
// const count_default = document.getElementById('count').value;
// var total_project = data.project.length;
// var count_row = count_default;
// var total_page = Math.ceil(total_project / count_row);;
// var current_page = 1;
// var project = data.project;
// var dev = data.dev;

// function getPropertyData(data) {
//     let propertyData = Object.getOwnPropertyNames(data[0]);
//     propertyData.push("Action");
//     propertyData = propertyData.filter(function(item) {
//         return item != "link";
//     })
//     return propertyData
// }
// class Pagination {
//     constructor(data, count_row, current_page, showValue, tableId) {
//         this.count_row = count_row;
//         this.tableId = tableId;
//         this.showValue = showValue;
//         this.data = data;
//         this.current_page = current_page;
//         this.total_page = total_page;
//         this.paginationInit();

//     }
//     paginationInit() {
//         this.btn_pre();
//         this.btn_next();
//         this.update_total_page();
//         this.load_page_number();
//         this.load_data(0);
//         this.change_page();
//     }
//     update_total_page() {
//         let select = document.getElementById('count');
//         this.count_row = select.options[select.selectedIndex].value;
//         this.total_page = Math.ceil(this.data.length / this.count_row);
//         return this.total_page, this.count_row

//     }
//     btn_next() {
//         var btn_next = document.querySelector(`.btn-next${this.tableId}`);
//         btn_next.addEventListener('click', () => {
//             //current_page++;
//             if (this.current_page < this.total_page) {
//                 this.current_page++;
//             }
//             this.update_total_page();
//             var start = (this.current_page - 1) * this.count_row;
//             this.load_data(start);
//             $(`.page-number${this.tableId} li`).removeClass('active')
//             $(`.page-number${this.tableId} li:nth-child(${this.current_page})`).addClass('active');

//         })

//     }
//     btn_pre() {
//         var a = this.tableId
//         var btn_pre = document.querySelector(`.btn-pre${this.tableId}`);

//         btn_pre.addEventListener('click', () => {
//             if (this.current_page > 1) {
//                 this.current_page--;

//             } else {
//                 $(`.btn-pre${this.tableId}`).prop('disabled', true)
//             }
//             this.update_total_page();
//             var start = (this.current_page - 1) * this.count_row;
//             this.load_data(start);
//             $(`.page-number${this.tableId} li`).removeClass('active')
//             $(`.page-number${this.tableId} li:nth-child(${this.current_page})`).addClass('active');
//         })
//     }

//     load_data(start) {
//         let html = '<tr>';
//         let end = parseInt(this.count_row) + parseInt(start);
//         let dataView = this.data.slice(start, end);
//         let propertyData = [];
//         try {
//             propertyData = Object.getOwnPropertyNames(dataView[0]);
//         } catch (error) {

//         }
//         propertyData = propertyData.filter(function(item) {
//             return item != "link";
//         })
//         let action = ['<div class="btn-group-sm"><button type="button" class="btn btn-primary btn-func">Update</button><button type="button" class="btn btn-danger">Remove</button></div>', '<div class="btn-group-sm"><button type="button" class="btn btn-primary btn-func">Update</button><label class="switch"><input type="checkbox" checked><span class="slider round"></span></label></div>'];
//         for (let i of dataView) {
//             for (let j of propertyData) {
//                 html += '<td ';
//                 if (j == "name" || j == "Dev") {
//                     html += `style="cursor:pointer">${i[j]}`;
//                 } else {
//                     html += `>${i[j]}`;
//                 }
//                 html += '</td>'
//             }

//             html += `
//                 <td>${action[this.showValue]}</td>
//                 </tr>`;

//         }
//         $(`#tbody${this.tableId}`).html($(html));

//         $("#totalTable tr td:nth-child(2), td:nth-child(6)").hover(function() {
//             $(this).css("text-decoration", "underline");
//         }, function() {
//             $(this).css("text-decoration", "none");
//         })


//     }

//     change_page() {
//         let current_pages = document.querySelectorAll(`.page-number${this.tableId} li`);
//         for (let i = 0; i < current_pages.length; i++) {
//             current_pages[i].addEventListener('click', () => {
//                 this.current_page = i + 1;
//                 this.load_data(i * this.count_row)
//                 $(`.page-number${this.tableId} li`).removeClass('active')
//                 $(`.page-number${this.tableId} li:nth-child(${this.current_page})`).addClass('active');
//             })
//         }
//     }
//     load_page_number() {
//         let $html = '<li class="page-item active"><a class="page-link" href="#">1</a></li>';
//         for (let i = 2; i <= this.total_page; i++) {
//             $html += '<li class="page-item"><a class="page-link" href="#">' + i + '</a></li>';
//         }
//         $(`#page-number${this.tableId}`).html($html);
//     }
//     setUp() {
//         this.update_total_page();
//         this.load_page_number();
//         this.load_data(0);
//         this.change_page();
//     }

// }

// function setPagSelect(pag) {
//     pag.current_page = 1;
//     pag.count_row = count_row;
//     pag.setUp();
// }
// // select number of row
// function select_count() {
//     var count_row = document.getElementById('count').value;
//     setPagSelect(pagination0);
//     setPagSelect(pagination1);
//     filter();
// }

// // select project/dev
// function selectShow() {}

// function filterData(dataset) {
//     let dataSearchProject = [];
//     let dataFilter = dataset;
//     let input = document.getElementById("search");
//     let filter = input.value.toUpperCase();
//     dataSearchProject = dataFilter.filter(function(i) {
//         return i.name.toUpperCase().indexOf(filter) > -1
//     })
//     return dataSearchProject
// }

// function setDataFilter(table, dataset) {
//     table.data = dataset;
//     table.current_page = 1;
//     table.pagination();
// }

// function filter() {
//     setDataFilter(table0, filterData(pagination0.data))
//     setDataFilter(table1, filterData(pagination1.data))
// }
$(function() {
    $(".datepicker").datepicker({
        dateFormat: 'yy-mm-dd'
    });
});
// $('#btnClearSearchDate').on('click', function() {
//     document.getElementById('startDate').value = '';
//     document.getElementById('endDate').value = '';
//     document.getElementById('search').value = '';
//     dataSearchDate = [];
//     let select = parseInt(document.getElementById('selectShow').value);
//     setDataFilter(table0, filterData(project));
//     setDataFilter(table1, filterData(dev));
// })

// class Table {
//     constructor(data, count_row, current_page, tableId, tableName) {
//         this.current_page = current_page;
//         this.count_row = count_row;
//         this.data = data;
//         this.tableId = tableId;
//         this.tableName = tableName;
//         this.tableInit();

//     }

//     tableInit() {
//         let thead = '<tr>';
//         let propertyData = getPropertyData(this.data);
//         for (let i of propertyData) {
//             console.log(i)
//             thead += `<th>${i.toUpperCase()}</th>`;
//         }
//         thead += '</tr>';
//         let $html = `<h3 class="project-name" id="projectName">${this.tableName}</h3>
//         <div class="table-project table-responsive">
//         <table class="table table-bordered table-hover text-center " id="table${this.tableId}">
//             <thead id="thead${this.tableId}">
//             ${thead}
//             </thead>
//             <tbody id="tbody${this.tableId}">
//             </tbody>
//         </table>
//         <footer class="row">
//             <div class="col-3">
//                 <ul id="pagination${this.tableId}" class="pagination">

//                     <li class="page-item${this.tableId}"><a class="page-link btn-pre${this.tableId}" href="#">Previous</a></li>
//                     <nav id="page-number${this.tableId}" class="page-number page-number${this.tableId}">
//                     </nav>
//                     <!-- <li class="page-item"><a class="page-link" href="#">1</a></li>
//                     <li class="page-item"><a class="page-link" href="#">2</a></li>
//                     <li class="page-item"><a class="page-link" href="#">3</a></li>-->
//                     <li class="page-item"><a class="page-link btn-next${this.tableId}" href="#">Next</a></li>
//                 </ul>
//             </div>
//         </footer>
//     </div>`
//             //document.getElementById('totalTable').append(html);
//         $('.totalTable').append($html);
//     }
//     pagination() {

//         let pag = new Pagination(this.data, this.count_row, this.current_page, this.tableId, this.tableId);
//         return pag;
//     }

// }
// /*var table0 = new Table(project, 3, 1, "0", "Project List")
// var pagination0 = table0.pagination();
// var table1 = new Table(dev, 3, 1, "1", "Developer List")
// var pagination1 = table1.pagination();
// */



// $(".switch input").click(function() {
//     let index = $(this).closest("tr").index();
//     let status = $(this).closest("tr").find(`td:eq(2)`);

//     let setStatus = 1 - parseInt(status.text())
//     $(this).closest("tr").find(`td:eq(2)`).text(setStatus)
// })