
<script type="text/javascript">
  $(document).ready(function() {
    $('#id_grade').on('change', function() {
      var grade = $(this).val();
      $.ajax({
        url: '/update_subgrade_choices/',
        data: {
          'grade': grade
        },
        success: function(data) {
          var subGradeSelect = $('#id_sub_grade');
          subGradeSelect.empty();
          $.each(data.subgrades, function(index, value) {
            subGradeSelect.append($('<option>').text(value).attr('value', index));
          });
        }
      });
    });
  });
</script>
