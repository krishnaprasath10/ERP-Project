




function datewisefilterfunction() {
    
        var datta = $("#datepicker").val();
        console.log(datta);
      
     
          $.ajax({
            url: '/attendance_filter/',
            type: 'POST',
            dataType: 'json',
            data: {date: datta, 'csrfmiddlewaretoken': '{{ csrf_token }}'},
            success: function(response) {
              console.log(response)
              
              var tableBody = $('#tableBody');
              tableBody.empty();
    
              for (var i = 0; i < response.length; i++) {
                var rowData = response[i];
            var row = '<tr>' +
              '<td style="text-align:center;">'+'<input type="checkbox" name="" value="">'+'</td>' +

             ' <td id="id"  style="text-align:center;">'+
            '<div class="d-flex flex-column justify-content-center">'+
            '<h6 class="mb-0 text-sm">' + rowData.id +'</h6>'+
            '</div>'+'</td>'+

            '<td id="employee_name" >'+
            '<div class="d-flex flex-column justify-content-center">'+
            '<h6 class="mb-0 text-sm">'+'<input type="name" style="border-style:none;background-color:white;" class="form-control" name="employee_name" id="Emp_name" value="' + rowData.Employee_Name +'" readonly>'+'</h6>'+
            ' </div>'+'</td>'+
          

             '<td style="width:3%;text-align:center;">'+
             '<div class="d-flex flex-column justify-content-center">'+
               '<h6 class="mb-0 text-sm">'+'<input type="number" style="border-style:none;background-color:white;text-align:center;" class="form-control" name="working_hours" id="wrking_hour" value="' + rowData.Working_Hours +'" readonly>'+'</h6>'+
            '</div>'+'</td>'+

              '<td style="width:4%;">'+'<div class="d-flex flex-column justify-content-center">'+
                '<h6 class="mb-0 text-sm"><input type="number" class="form-control" name="worked_hours" id="wrked_hour" value="0">' + '<h6>'+
              '</div>'+'</td>' +

              '<td style="width:4%;>' +'<div class="d-flex flex-column justify-content-center">'+
                '<h6 class="mb-0 text-sm">'+'<input type="number" class="form-control" name="over_time" id="ovrtime" value="0">'+'</h6>'+
              '</div>'+'</td>'+

              '<td style="width:4%;border-style:none;">' +'<div class="d-flex flex-column justify-content-center">'+
                '<h6 class="mb-0 text-sm">'+'<input type="number" class="form-control" name="permission" id="prmison" value="0">'+'</h6>'+
               '</div>'+'</td>' +

              '<td style="width:3%;text-align:center;" value = 0 name="cl" id="clv">' +'<div class="d-flex flex-column justify-content-center">'+
                '<h6 class="mb-0 text-sm">'+'</h6>'+
               '</div>'+'</td>' +

               '<td style="width:3%;text-align:center;" value = 0 name="sl" id="slv">' +'<div class="d-flex flex-column justify-content-center">'+
                '<h6 class="mb-0 text-sm">'+'</h6>'+
               '</div>' +'</td>' +

               '<td>'+
                '<input type="name" style="border-style:none;background-color:white;" class="form-control" id="sts" name="status" value="-NA-" id="floatingInput" readonly>'+'</h6>'+
                '</td>'+

                '<td id="Attendance">' +
                  '<button style="padding: 6px 6px;" data-id="' + rowData.id + '" type="button" onclick="presentfunction(this)" value="Present" class="btn btn-success">Present</button>' +
                 '&nbsp;'+'<button style="padding: 6px 6px;" data-id="' + rowData.id + '" type="button" onclick="Absentfunction(this)" value="Absent" class="btn btn-danger">Absent</button>' +
                 '&nbsp;'+'<button style="padding: 6px 6px;" data-id="' + rowData.id + '" type="button" onclick="Casualfunction(this)" value="Casual" class="btn btn-info">Casual</button>' +
                 '&nbsp;'+'<button style="padding: 6px 6px; width: 20%;" data-id="' + rowData.id + '" type="button" onclick="Sickfunction(this)" value="Sick" class="btn btn-warning">Sick</button>' +
                '</td>';
              '</tr>';
            tableBody.append(row);
          }
        }
      });
    
  }

