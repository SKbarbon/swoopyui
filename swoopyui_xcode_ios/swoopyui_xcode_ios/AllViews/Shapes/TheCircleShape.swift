//
//  TheCircleShape.swift
//  swoopyui
//
//  Created by Yousif Aladwani on 25/05/2023.
//

import SwiftUI

struct TheCircleShape: View {
    @State var host_port : Int
    @State var textData : SwoopyView
    var body: some View {
        Circle ()
            .frame(width: CGFloat(textData.width!), height: CGFloat(textData.height!))
            .foregroundColor(getColorFromString(colorName: textData.fgcolor!))
    }
}
