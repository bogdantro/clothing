window.addEventListener("scroll", function(){
  const navbar = document.getElementById('mobileNav');
  navbar.classList.toggle("sticky", window.scrollY > 1)
})

window.addEventListener("scroll", function(){
  const navbar = document.getElementById('desNav');
  navbar.classList.toggle("sticky", window.scrollY > 1)
})


function menu(){
  const sidebar = document.getElementById('sidebar');
  const navbar = document.getElementById('mobileNav');
  const hamburger = document.getElementById('hamburger');

  const help = document.getElementById('helpDropdown');
  const helpToggle = document.getElementById('helpToggle');

  const searchBar = document.getElementById('searchBar');
  const searcIcon = document.getElementById('searcIcon');


  if (window.getComputedStyle(sidebar,null).getPropertyValue("opacity") == '0'){
    navbar.classList.add('menu')  
    hamburger.classList.add('click')  
    sidebar.classList.add('active')
    searchBar.classList.remove('active')
    searcIcon.classList.remove('active')
  } else{
    navbar.classList.remove('menu') 
    hamburger.classList.remove('click')  
    sidebar.classList.remove('active')
    help.classList.remove('active')
    helpToggle.classList.remove('click')
  }  
};

// ABOUT DROPDOWN
function help(){
  const helpToggle = document.getElementById('helpToggle');
  const help = document.getElementById('helpDropdown');


  if (window.getComputedStyle(help,null).getPropertyValue("display") == 'none'){
    help.classList.add('active')
    helpToggle.classList.add('click')
  } else{
    help.classList.remove('active')
    helpToggle.classList.remove('click')
  }
}

// search
function search(){
  const searchBar = document.getElementById('searchBar');
  const searcIcon = document.getElementById('searcIcon');
  const navbar = document.getElementById('mobileNav');

  if (window.getComputedStyle(searchBar,null).getPropertyValue("opacity") == '0'){
    searchBar.classList.add('active')
    searcIcon.classList.add('active')
    navbar.classList.add('search')
    document.getElementById("searchInput").focus();
    document.body.style.overflow = "hidden";
    document.documentElement.style.overflow = "hidden";
  }else{
    searchBar.classList.remove('active')
    searcIcon.classList.remove('active')
    navbar.classList.remove('search')
    document.body.style.overflow = "scroll";
    document.documentElement.style.overflow = "scroll";
  }
}

// $(function popularD(){
  //   const popularTitleD = document.getElementById('popularTitleD');
  //   $(popularTitleD).hover(function(){
  //     $(popularTitleD).css('background','rgba(245, 245, 245, 0.2)') 
  //     $('#popularD').css('display','block') 
  //   },function(){
  //     setTimeout(function() { 
  //       $(popularTitleD).css('background','') 
  //       $('#popularD').css("display","none")
  //     }, 100);
  //   })
  // });