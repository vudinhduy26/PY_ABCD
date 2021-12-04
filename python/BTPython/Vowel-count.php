<?php

function getCount($str) {
    $vowelsCount = 0;
    $vowelArr = ['a','e','i','o','u'];
    $strSplit = str_split($str,1);
    
    for( $i=0; $i < count($strSplit); $i++){
      if( in_array($strSplit[$i], $vowelArr)) 
        $vowelsCount++;
    }
    
    return $vowelsCount;
  }
?>