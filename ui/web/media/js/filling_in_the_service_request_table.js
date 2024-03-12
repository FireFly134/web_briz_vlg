let rowCounter = 1; // Счетчик номера п/п
	//
	function formatDate(date) {
    const options = { day: 'numeric', month: 'numeric', year: 'numeric', hour: 'numeric', minute: 'numeric' };
    return new Intl.DateTimeFormat('ru-RU', options).format(date);
}
	function addTableRow(id, address, num_house, entrance, flat_or_tel, date_time_accepted, dispatcher, mechanics, date_time_closed, malfunction_and_cause, description, status, date_time_transfer, simple) {
		// Форматирование даты date_time_accepted
		const formattedDateAccepted = date_time_accepted !== 'None' ? formatDate(new Date(date_time_accepted)) : '';

		// Форматирование даты date_time_transfer
		const formattedDateTransfer = date_time_transfer !== 'None' ? formatDate(new Date(date_time_transfer)) : '';

		// Проверка и форматирование даты date_time_closed
		const formattedDateClosed = date_time_closed !== 'None' ? formatDate(new Date(date_time_closed)) : '';

		const edit_url = `/malfunctions/edit/${id}`
		const send_archive_url = `/malfunctions/send_archive/${id}`
		const send_black_url = `/malfunctions/send_black/${id}`
		const newRow = tbody.insertRow();
		const cell1 = newRow.insertCell(0);
		const cell2 = newRow.insertCell(1);
		const cell3 = newRow.insertCell(2);
		const cell4 = newRow.insertCell(3);
		const cell5 = newRow.insertCell(4);
		const cell6 = newRow.insertCell(5);
		const cell7 = newRow.insertCell(6);
		const cell8 = newRow.insertCell(7);
		const cell9 = newRow.insertCell(8);
		const cell10 = newRow.insertCell(9);
		const cell11 = newRow.insertCell(10);
		const cell12 = newRow.insertCell(11);
		const cell13 = newRow.insertCell(12);
		const cell14 = newRow.insertCell(13);
		const cell15 = newRow.insertCell(14);

		cell1.textContent = rowCounter++;
		cell2.textContent = address;
		cell3.textContent = num_house;
		cell4.textContent = entrance;
		cell5.textContent = flat_or_tel;
		cell6.textContent = dispatcher;
		cell7.textContent = formattedDateAccepted;
		cell8.textContent = mechanics;
		cell9.textContent = formattedDateTransfer;
		cell10.textContent = formattedDateClosed;
		cell11.textContent = simple !== 'None' ? simple : '';
		cell12.textContent = malfunction_and_cause !== 'None' ? malfunction_and_cause : '';
		cell13.textContent = description !== 'None' ? description : '';
		cell15.textContent = status;
		cell15.style.display = "none";


		// Создаем ссылку для редактирования
		const editLink = document.createElement("a");
		editLink.href = edit_url;
		editLink.className = "btn btn-link";
		editLink.title = "Редактировать";

		// Создаем иконку для редактирования
		const editIcon = document.createElement("i");
		editIcon.className = "fas fa-pencil-alt";

		// Добавляем иконку в ссылку
		editLink.appendChild(editIcon);

		// Создаем ссылку для переноса в архив
		const send_archive_link = document.createElement("a");
		send_archive_link.href = send_archive_url;
		send_archive_link.className = "btn btn-link add_archive";
		send_archive_link.title = "закрыть заявку и переместить в архив";
		send_archive_link.style.display = "";

		// Создаем иконку для переноса в архив
		const send_archive_icon = document.createElement("i");
		send_archive_icon.className = "fas fa-folder-plus";

		// Добавляем иконку в ссылку
		send_archive_link.appendChild(send_archive_icon);

		// Создаем ссылку для переноса из архива назад
		const send_black_link = document.createElement("a");
		send_black_link.href = send_black_url;
		send_black_link.className = "btn btn-link del_archive";
		send_black_link.title = "открыть заявку и переместить в активные";
		send_black_link.style.display = "none";

		// Создаем иконку для переноса в архив
		const send_black_icon = document.createElement("i");
		send_black_icon.className = "fas fa-folder-minus";

		// Добавляем иконку в ссылку
		send_black_link.appendChild(send_black_icon);

		// Добавляем ссылки в ячейку
		cell14.appendChild(editLink);
		cell14.appendChild(send_archive_link);
		cell14.appendChild(send_black_link);
	}