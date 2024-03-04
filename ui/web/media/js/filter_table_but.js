var index = -1; // Индекс столбца для status

  /////////////////////////////////////////////////////////////////////////////////////////////////
 //Фильтр по значениям в таблице открыт договор и строительная готовность, работает через кнопки//
/////////////////////////////////////////////////////////////////////////////////////////////////
function filterTableButton(status_value="True") {
  var table, tr, td;
  table = document.getElementById("Table");
  tr = table.getElementsByTagName("tr");

  let button1 = document.getElementById("btn-group-1");
  let button2 = document.getElementById("btn-group-2");
  let add_archive = document.getElementsByClassName("add_archive");
  let del_archive = document.getElementsByClassName("del_archive");
  if (status_value === "True"){
        button1.className = 'btn btn-primary mt-3';
        button2.className = 'btn btn-secondary mt-3';
        for (var i = 0; i < add_archive.length; i++){
            add_archive[i].style.display = "";
            del_archive[i].style.display = "none";
            }
  }else{
        button1.className = 'btn btn-secondary mt-3';
        button2.className = 'btn btn-primary mt-3';
        for (var i = 0; i < add_archive.length; i++){
            add_archive[i].style.display = "none";
            del_archive[i].style.display = "";
            }
  }

  if (index === -1){
      // Находим заголовочную строку таблицы (первую строку)
      var headerRow = tr[1];
      td = headerRow.getElementsByTagName("td");

      // Ищем индексы столбцов, соответствующих поиску

      for (var j = 0; j < td.length; j++) {
        var headerText = td[j].textContent || td[j].innerText;
        if (headerText.trim() === "status") {
           window.index = j;
        }
      }
  }
  var npp = 0;
    console.log(window.index)
  // Проходим по каждой строке таблицы, начиная с индекса 2 (пропускаем первые две строки)
  for (var i = 2; i < tr.length; i++) {
    td = tr[i].getElementsByTagName("td");
    // Получаем содержимое ячеек в нужных столбцах
    var StatusValue = td[index].textContent || td[index].innerText;

    // Проверяем значения и скрываем строки, если необходимо
    if (StatusValue.trim() === status_value) {
      npp++;
      td[0].textContent = npp;
      tr[i].style.display = "";
    } else {
      tr[i].style.display = "none";
    }
  }
  };
