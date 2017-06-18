var ballotview =
{
  init:function(){
    ballotview.view.displayBallotView();
    },
  services:{
    getBallotView: function (){
      return $.ajax({
        method: 'GET',
        url: '/templates/ballot'
      });
    },
    getBallotData: function (){
      return mock_ballot_data;
    }
  },
  events:{},
  view:{
    displayBallotView: function(){
      $.when( ballotview.services.getBallotView(),
              ballotview.services.getBallotData()).done(
                function(template_raw, ballot_data){
                    var template = Handlebars.compile(template_raw[0]);
                    var html = template(ballot_data);
                    $('#ballot-display').html(html);
                });

    }
  }
}

$(ballotview.init());
