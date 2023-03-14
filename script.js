function submitUsername() {
    const usernameInput = document.getElementById("username");
    const username = usernameInput.value;
  
    // 从数据库中获取用户信息
    fetch(`http://localhost:001/users/${username}`)
      .then(response => response.json())
      .then(data => {
        const { seg_flight, seg_dep_time, seg_route_from, seg_route_to } = data;
        // 创建表格并显示用户信息
        const table = document.createElement("table");
        const row1 = table.insertRow();
        const row2 = table.insertRow();
  
        const cell1 = row1.insertCell();
        const cell2 = row1.insertCell();
        const cell3 = row2.insertCell();
        const cell4 = row2.insertCell();
  
        cell1.innerHTML = "Flight";
        cell2.innerHTML = "Departure Time";
        cell3.innerHTML = "Route From";
        cell4.innerHTML = "Route To";
  
        const flightCell = row1.insertCell();
        flightCell.innerHTML = seg_flight;
        const depTimeCell = row1.insertCell();
        depTimeCell.innerHTML = seg_dep_time;
        const fromCell = row2.insertCell();
        fromCell.innerHTML = seg_route_from;
        const toCell = row2.insertCell();
        toCell.innerHTML = seg_route_to;
  
        const userInfoDiv = document.getElementById("userinfo");
        userInfoDiv.appendChild(table);
      });
  }
  

document.getElementById("member-submit-button").addEventListener("click", function() {
    // 处理购买会员月付制表单的提交
});

document.getElementById("seat-submit-button").addEventListener("click", function() {
    // 处理选座表单的提交
});

  function calculatePrice() {
    var membershipType = document.getElementById("membership-type").value;
    var membershipDuration = document.getElementById("membership-duration").value;
    var price = 0;
    
    if (membershipType === "basic") {
      if (membershipDuration === "6") {
        price = 1200;
      } else if (membershipDuration === "12") {
        price = 2000;
      } else if (membershipDuration === "24") {
        price = 3500;
      }
    } else if (membershipType === "premium") {
      if (membershipDuration === "6") {
        price = 2400;
      } else if (membershipDuration === "12") {
        price = 4200;
      } else if (membershipDuration === "24") {
        price = 7500;
      }
    }
    
    document.getElementById("price").innerHTML = "价格：" + price + "￥";
    
  }

  const seatMap = {
    J: [
      ["1A", "1B", "1C", "1D", "1E", "1F", "1G", "1H"],
      ["2A", "2B", "2C", "2D", "2E", "2F", "2G", "2H"],
      ["3A", "3B", "3C", "3D", "3E", "3F", "3G", "3H"],
      ["4A", "4B", "4C", "4D", "4E", "4F", "4G", "4H"],
      ["5A", "5B", "5C", "5D", "5E", "5F", "5G", "5H"],
    ],
    Y: [
      ["1A", "1B", "1C", "1D", "1E", "1F", "1G", "1H", "1I", "1J"],
      ["2A", "2B", "2C", "2D", "2E", "2F", "2G", "2H", "2I", "2J"],
      ["3A", "3B", "3C", "3D", "3E", "3F", "3G", "3H", "3I", "3J"],
      ["4A", "4B", "4C", "4D", "4E", "4F", "4G", "4H", "4I", "4J"],
      ["5A", "5B", "5C", "5D", "5E", "5F", "5G", "5H", "5I", "5J"],
    ],
  };
  
  let selectedSeat = null;
  let selectedLevel = null;
  let selectedSeat1 = null;
  
  function showSeatMap() {
    selectedLevel = document.getElementById("seat-level").value;
    const seatTableBody = document.querySelector("#seat-map table tbody");
    seatTableBody.innerHTML = "";
    seatMap[selectedLevel].forEach(row => {
      const newRow = document.createElement("tr");
      row.forEach(seat => {
        const newCell = document.createElement("td");
        const newButton = document.createElement("button");
        newButton.textContent = seat;
        newButton.addEventListener("click", () => {
            selectedSeat1 = `${seat}`;
            selectedSeat = `${selectedLevel}${seat}`;
            document.querySelector("#selected-seat").textContent = `已选座位：${selectedSeat}`;
          });
        newCell.appendChild(newButton);
        newRow.appendChild(newCell);
      });
      seatTableBody.appendChild(newRow);
    });
    document.getElementById("seat-map").style.display = "block";
  }
  
  function selectSeat() {
    let price = 0;
    if (selectedLevel === "J") {
      price = 100;
    } else if (selectedLevel === "Y") {
      price = 50;
    }
    selectedLevel = document.getElementById("seat-level").value;
    submited_seat = `${selectedLevel}${selectedSeat1}`;
    document.querySelector("#seat-output").textContent = `已提交座位：${submited_seat}`
    document.querySelector("#seat-output").style.display = "block";
    document.querySelector("#price-output").textContent = `付费选座价格：${price}￥`;
    document.querySelector("#price-output").style.display = "block";
    document.getElementById("seat-select-button").style.display = "none";
  }

  