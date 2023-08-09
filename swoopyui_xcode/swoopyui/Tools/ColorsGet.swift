//
//  ColorsGet.swift
//  swoopyui
//
//  Created by Yousif Aladwani on 19/05/2023.
//

import Foundation
import SwiftUI

func getColorFromString (colorName:String) -> Color {
    if colorName.starts (with: "#") {
        return Color(hex: colorName)
    }
    
    if colorName == "white" {
        return Color.white
    }else if colorName == "black" {
        return Color.black
    }else if colorName == "blue" {
        return Color.blue
    }else if colorName == "yellow" {
        return Color.yellow
    }else if colorName == "pink" {
        return Color.pink
    }else if colorName == "red" {
        return Color.red
    }else if colorName == "green" {
        return Color.green
    }
    
    return Color.primary
}

extension Color {
    init(hex: String) {
        let scanner = Scanner(string: hex)
        var rgbValue: UInt64 = 0

        scanner.scanHexInt64(&rgbValue)

        let r = Double((rgbValue & 0xFF0000) >> 16) / 255.0
        let g = Double((rgbValue & 0x00FF00) >> 8) / 255.0
        let b = Double(rgbValue & 0x0000FF) / 255.0

        self.init(red: r, green: g, blue: b)
    }
}
