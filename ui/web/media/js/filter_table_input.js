	function NullFilterTable() {
	// Обновляем значение скрытого поля
		document.getElementById('filterInput').value = '';
		filterTable()
		}
	function filterTable(inputElement = document.getElementById("filterInput").value) {
	  var filter, table, tr, td, i, j, txtValue;
	  filter = inputElement.toUpperCase();
	  table = document.getElementById("Table");
	  tr = table.getElementsByTagName("tr");

	  // Проходим по каждой строке таблицы, начиная с индекса 2 (пропускаем первые две строки)
	  for (i = 1; i < tr.length; i++) {
		td = tr[i].getElementsByTagName("td");
		var rowVisible = false;
		for (j = 0; j < td.length; j++) {
		  if (td[j]) {
			txtValue = td[j].textContent || td[j].innerText;

			if (txtValue.toUpperCase().indexOf(filter) > -1) {
			  rowVisible = true;
			  break;
			}
		  }
		}

		// Показываем или скрываем строку в зависимости от значения флага
		tr[i].style.display = rowVisible ? "" : "none";
	  }
	}
	function handleInput(event) {
		filterTable(event.target.value);
	}