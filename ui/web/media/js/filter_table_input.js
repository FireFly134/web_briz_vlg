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

	document.addEventListener("DOMContentLoaded", function () {
		let tbody = document.getElementById('tbody');

		{% for item in list %}
			addTableRow(`{{ item.id|safe }}`, `{{ item.address|safe }}`, `{{ item.num_house|safe }}`, `{{ item.entrance|safe }}`, `{{ item.flat_or_tel|safe }}`, `{{ item.date_time_accepted|safe }}`, `{{ item.dispatcher|safe }}`, `{% for mechanic in item.mechanics.all %}{{ mechanic.fio|safe }}{% if not forloop.last %}\n{% endif %}{% endfor %}`, `{{ item.date_time_closed|safe }}`, `{{ item.malfunction_and_cause|safe }}`, `{{ item.transfer_of_the_application|safe }}`, `{{ item.description|safe }}`, `{{ item.status|safe }}`, `{{ item.date_time_transfer|safe }}`, `{{ item.simple|safe }}`);
		{% endfor %}
	});